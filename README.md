# Run the application using Docker Compose
The main folder of this repository contains a functional docker-compose.yml file. Run the application using it as shown below:

```
$ curl -sSL https://raw.githubusercontent.com/the-harpia-io/harp-agent/master/docker-compose.yml > docker-compose.yml
$ curl -sSL https://raw.githubusercontent.com/the-harpia-io/harp-agent/master/config.yaml > config.yaml
$ docker-compose up -d
```

# Configuration
- NOTIFICATIONS_SCRAPE_INTERVAL_SECONDS: How often scrape alerts from monitoring systems
- GATE_HOST: Harp gateway to receive alerts from agent