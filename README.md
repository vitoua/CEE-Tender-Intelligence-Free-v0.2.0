# CEE Tender Intelligence Free v0.2.0

Zero-cost Render edition. It uses one Free Web Service only: no PostgreSQL, no disk, no cron job. Tender data is loaded manually from Prozorro/TED and held only in memory. Because Render Free sleeps after inactivity and has an ephemeral filesystem, cached tenders disappear after sleep, restart, or deploy. Refresh the sources again after wake-up.

## Render deployment
1. Push all files to the root of a GitHub repository.
2. In Render choose New > Blueprint and select the repository.
3. Enter ADMIN_EMAIL and ADMIN_PASSWORD.
4. Apply the Blueprint.
5. Open /health, then sign in and select Refresh Prozorro / Refresh TED.

## Local
```bash
cp .env.example .env
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Deliberately removed
- PostgreSQL and SQLite persistence
- scheduled cron synchronization
- persistent KAM/user management and tender statuses

These features require durable storage and therefore are outside this strictly free, stateless edition.
