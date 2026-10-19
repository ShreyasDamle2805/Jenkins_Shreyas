# Jenkins CI/CD: Flask and Express on EC2

This project contains two applications in one GitHub repository:

**Repository:** [Jenkins_Shreyas](https://github.com/ShreyasDamle2805/Jenkins_Shreyas)

| Application folder | Service | Port | Homepage | Health check |
| --- | --- | ---: | --- | --- |
| `flask-backend/` | Flask backend | 5000 | `/` | `/api/health` |
| `express-frontend/` | Express app | 3000 | `/` | `/health` |

The Jenkins pipelines install dependencies, run tests, and use PM2 to start or
restart each service. Configure the Jenkins agent on the same EC2 instance as
the applications, or on an agent with equivalent access.

## Project layout

```text
Jenkins_CICD_Shreyas_Damle/
├── flask-backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── test_app.py
│   └── Jenkinsfile
├── express-frontend/
│   ├── server.js
│   ├── package.json
│   ├── package-lock.json
│   ├── test.js
│   └── Jenkinsfile
├── evidence/
│   └── README.md
├── Jenkins_CICD_Shreyas_Damle_Documentation.docx
└── README.md
```

## 1. Prepare the EC2 instance

These commands assume a fresh Ubuntu EC2 instance. Choose an instance size
suitable for Jenkins and both applications. Running Jenkins on the same small
instance can exceed free-tier memory limits.

```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip curl fontconfig openjdk-21-jre
```

Install Node.js 20 LTS and PM2 using the official NodeSource setup for Ubuntu:

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
sudo npm install --global pm2
```

Install Jenkins from the official Jenkins Debian repository using the current
instructions at https://www.jenkins.io/doc/book/installing/linux/. The Jenkins
service needs Java. Allow inbound traffic only from trusted IPs for SSH (22)
and Jenkins (8080); allow app ports 3000 and 5000 only from intended clients.
Do not expose Jenkins or SSH to the entire internet.

## 2. Publish and clone the repository

The provided GitHub repository URL is
https://github.com/ShreyasDamle2805/Jenkins_Shreyas. It is a single repository
containing both application folders. The project files are being published to
its `main` branch; use the repository root as the Jenkins SCM source.

The Jenkins jobs check out the repository and install each application's
dependencies in their workspace; a separate manual clone or startup is not
needed. The deployment pipelines run PM2 as the Jenkins service user. To
restore that user's saved process list after an EC2 reboot, configure PM2
startup for the `jenkins` user and execute the exact `sudo ...` command PM2
prints.

Verify both services locally:

```bash
curl --fail http://127.0.0.1:5000/api/health
curl --fail http://127.0.0.1:3000/health
sudo -u jenkins -H pm2 status
```

## 3. Configure Jenkins pipelines

Install Jenkins Pipeline, Git, and GitHub integration plugins. Create two
Pipeline-from-SCM jobs, both using this repository and branch `main`:

1. `flask-backend`: script path `flask-backend/Jenkinsfile`.
2. `express-frontend`: script path `express-frontend/Jenkinsfile`.

Both Jenkinsfiles check out the monorepo and run commands from their own
application subfolder. The Jenkins agent must have `git`, `python3`,
`python3-venv`, `pip`, `node`, `npm`, `pm2`, and `curl` in its PATH. The agent
user needs permission to run PM2 and own the application processes. Configure
PM2 startup for that same account if the apps must survive an EC2 reboot.
The Jenkinsfiles set `JENKINS_NODE_COOKIE=dontKillMe` when starting or
restarting PM2 processes so Jenkins does not terminate the deployed services
when a build finishes.

Each pipeline checks out the repository, installs dependencies, runs tests,
deploys with PM2, then calls its local health endpoint. A failed test or health
check fails that build. Both Jenkinsfiles declare the `githubPush()` trigger;
install the GitHub plugin and enable the GitHub hook trigger for Git polling
for each job if your Jenkins configuration requires the job-level trigger to
be enabled as well.

## 4. Configure a GitHub webhook

Since both pipelines use the same repository, configure one webhook in
**Settings → Webhooks → Add webhook**:

- Payload URL: `http://EC2_PUBLIC_DNS_OR_IP:8080/github-webhook/`
- Content type: `application/json`
- Events: **Just the push event**
- Active: enabled

Ensure Jenkins GitHub webhook support is configured and the EC2 security group
and host firewall allow inbound webhook traffic. Confirm a successful delivery
in GitHub and that a push starts the appropriate Jenkins job. Verify both jobs
are configured to build the `main` branch. For production, use HTTPS and
restrict webhook access.

## 5. Test locally before deployment

Flask (Python 3.9 or newer):

```bash
cd flask-backend
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/python -m pytest -q
```

Express (Node.js 18 or newer):

```bash
cd express-frontend
npm ci
npm test
```

## Architecture

```text
Developer push
     |
GitHub: ShreyasDamle2805/Jenkins_Shreyas
     | one push webhook
Jenkins (EC2, port 8080)
     | checkout / install / test / deploy
    PM2
   /   \
Flask :5000        Express :3000
/api/health          /health
```

## Submission evidence

The assignment documentation is in
`Jenkins_CICD_Shreyas_Damle_Documentation.docx`. The `evidence/` folder lists
the deployment status, supplied Jenkins build screenshots, and remaining
evidence to capture.

### Live verification (October 19, 2026)

Both Jenkins pipelines completed successfully on commit `f9637b4`:

- Flask build #6: success; 2 tests passed.
- Express build #3: success; 2 tests passed.
- PM2 showed both `flask-backend` and `express-frontend` online.
- `http://127.0.0.1:5000/api/health` and
  `http://127.0.0.1:3000/health` both returned `{"status":"healthy"}`.

The checked-in Jenkins screenshots and terminal verification record are in
`evidence/`. GitHub currently has no webhook configured for this repository.
Before calling the assignment complete, configure a push webhook, verify a
successful delivery triggers Jenkins, capture its delivery, and add genuine
EC2-console and terminal screenshots to `evidence/`. The current submission ZIP
contains the repository files and the evidence available so far; it does not
claim webhook verification or include screenshots that have not been captured.
