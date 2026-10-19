# Deployment evidence

## Verified on October 19, 2026

The original pipeline runs completed successfully from commit `f9637b4`:

- `03-jenkins-flask-build-6.png` — Flask build #6. Its final result was checked
  from Jenkins after the screenshot was taken.
- `04-jenkins-express-build-3.png` — Express build #3. Its final result was
  checked from Jenkins after the screenshot was taken.
- `01-ec2-instance-running.png` — EC2 console showing the instance in the
  running state. The AWS account identifier has been redacted in this copy.
- `05-github-webhook-settings-empty.png` — GitHub repository webhook settings
  page showing no webhook was configured when captured. This is not evidence
  of a successful webhook delivery.
- `02-ec2-app-health-checks.txt` — terminal verification record: PM2 showed
  both applications online and both local health endpoints returned healthy.
- `02-ec2-app-health-checks.png` — terminal screenshot showing both PM2
  processes online and both Flask and Express health endpoints returning
  `{"status":"healthy"}`.
- `06-github-webhook-push-delivery.txt` — GitHub reported HTTP 200 for the push
  delivery from commit `4e77fb9`; it triggered Flask build #7 and Express build
  #4, both of which finished `SUCCESS`. PM2 and both health endpoints were
  checked again after deployment.

The screenshots were supplied during the builds and show their Jenkins pages;
the final successful results were verified separately from Jenkins build logs.
The webhook delivery and resulting build outcomes were verified through the
GitHub API and Jenkins build logs.

Do not include passwords, access keys, tokens, Jenkins setup secrets, or other
credentials in screenshots.
