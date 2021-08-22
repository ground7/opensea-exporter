# opensea-exporter
Prometheus exporter for opensea

To run:

```bash
docker run -d --name opensea-exporter -p 9000:9000 --restart=unless-stopped opensea-exporter:latest
docker run -d --name prometheus -p 9090:9090 -v /home/josiah/git-repos/opensea-exporter/prometheus.yaml:/etc/prometheus/prometheus.yml prom/prometheus
docker run -d --name=grafana -p 3000:3000 -e "GF_INSTALL_PLUGINS=marcusolsson-json-datasource,dalvany-image-panel" grafana/grafana
```