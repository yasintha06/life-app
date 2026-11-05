-- My Life App: run this once in Supabase > SQL Editor > New query > Run.
-- One table holds everything. Row-level security means each signed-in person can only ever see and change their own rows.

create table if not exists public.docs (
  user_id    uuid        not null default auth.uid() references auth.users(id) on delete cascade,
  coll       text        not null,
  id         text        not null,
  data       jsonb       not null,
  updated_at timestamptz not null default now(),
  primary key (user_id, coll, id)
);

alter table public.docs enable row level security;

drop policy if exists "read own"   on public.docs;
drop policy if exists "add own"    on public.docs;
drop policy if exists "change own" on public.docs;
drop policy if exists "delete own" on public.docs;
create policy "read own"   on public.docs for select using (auth.uid() = user_id);
create policy "add own"    on public.docs for insert with check (auth.uid() = user_id);
create policy "change own" on public.docs for update using (auth.uid() = user_id) with check (auth.uid() = user_id);
create policy "delete own" on public.docs for delete using (auth.uid() = user_id);

-- Live sync between your phone and laptop
alter table public.docs replica identity full;
do $$ begin
  alter publication supabase_realtime add table public.docs;
exception when duplicate_object then null; end $$;
