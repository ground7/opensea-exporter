# opensea-exporter
Prometheus exporter for opensea

To run:

```bash
docker run --name opensea-exporter -p 9000:9000 --restart=unless-stopped opensea-exporter:latest
docker run --name prometheus -p 9090:9090 -v /home/josiah/git-repos/opensea-exporter/prometheus.yaml:/etc/prometheus/prometheus.yml prom/prometheus
```