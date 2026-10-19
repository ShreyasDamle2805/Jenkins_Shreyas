# Deployment evidence

## Verified on October 19, 2026

Both pipelines completed successfully from commit `f9637b4`:

- `03-jenkins-flask-build-6.png` — Flask build #6. Its final result was checked
  from Jenkins after the screenshot was taken.
- `04-jenkins-express-build-3.png` — Express build #3. Its final result was
  checked from Jenkins after the screenshot was taken.
- `02-ec2-app-health-checks.txt` — terminal verification record: PM2 showed
  both applications online and both local health endpoints returned healthy.

The screenshots were supplied during the builds and show their Jenkins pages;
the final successful results were verified separately from Jenkins build logs.

## Still required for complete assignment evidence

Capture these genuine screenshots from the actual deployment and add them here:

1. `01-ec2-instance-running.png` — EC2 console showing the instance running.
2. `02-ec2-app-health-checks.png` — terminal showing PM2 status and both
   successful local health checks. The included `.txt` file is a verification
   record, not a screenshot.
3. `05-github-webhook-delivery.png` — GitHub webhook delivery showing success
   and the resulting Jenkins trigger. No webhook was configured when this
   evidence set was prepared.

Do not include passwords, access keys, tokens, Jenkins setup secrets, or other
credentials in screenshots.
