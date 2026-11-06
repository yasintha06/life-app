# My Life App

Shifts and pay, money and credit cards, daily plan and habits, Azure studies, job applications, weekly and monthly reviews.
A single web page hosted free on GitHub Pages. Data lives in a free Supabase database behind your login.

## Files

- `index.html`: the whole app
- `setup.sql`: run once in Supabase to create the database table and its security rules
- `manifest.webmanifest`, `icon.svg`: lets you add it to your phone's home screen

## One-time setup

1. **Supabase**: create a free project at supabase.com. Open **SQL Editor › New query**, paste all of `setup.sql`, then press **Run**.
2. **Supabase › Authentication › URL Configuration**: set **Site URL** to `https://yasintha06.github.io/life-app/`.
3. **GitHub**: in this repo, open **Settings › Pages**. Set **Source** to *Deploy from a branch*, choose **main** and **/ (root)**, then save. The app appears at `https://yasintha06.github.io/life-app/` within a minute or two.
4. Open the app and paste your Supabase **Project URL** and **publishable key** (or anon public key). Both are under **Project Settings › API Keys**.
5. Press **Create account**, confirm your email, then sign in.
6. **Supabase › Authentication › Sign In / Providers**: turn off **Allow new users to sign up**, so nobody else can make an account.
7. In the Claude version of the app, go to **More › Backup › Download backup**. Then in this app, go to **More › Backup › Restore from file**.

## Safety

- Every row is locked to your user id by row-level security in `setup.sql`. The publishable key only works together with your login.
- Never put a `service_role` or `sb_secret_` key in the app or in this repo.
- Download a backup now and then from **More › Backup**.
- Free Supabase projects pause after about a week with no use. Open the Supabase dashboard and press **Restore** to wake it. Your data is kept.

## Changing the app

`src/app.html` is the app itself. `src/standalone-shim.html` adds the login and Supabase data layer. Run `python3 src/build.py` to rebuild `index.html`.
