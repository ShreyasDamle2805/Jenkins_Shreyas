# Required live evidence (capture after deployment)

This folder is intentionally empty of screenshots until a real EC2/Jenkins
deployment has been performed. Do not use mockups or screenshots from a
different project.

Add genuine, legible screenshots here and reference them in the project
documentation:

1. `01-ec2-instance-running.png` — EC2 console showing the instance state and
   instance identity. Hide account identifiers if desired.
2. `02-ec2-app-health-checks.png` — terminal on the deployed host showing
   `pm2 status` and successful `curl` calls to both local health endpoints.
3. `03-jenkins-flask-success.png` — Jenkins Flask job build summary and
   successful test/deploy/health-check stages.
4. `04-jenkins-express-success.png` — Jenkins Express job build summary and
   successful test/deploy/health-check stages.
5. `05-github-webhook-delivery.png` — optional but recommended successful
   GitHub webhook delivery for each repository.

Do not include passwords, access keys, tokens, Jenkins initial admin secrets,
or other credentials in screenshots.
