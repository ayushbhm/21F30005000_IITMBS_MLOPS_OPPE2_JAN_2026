# Deliverable 6: Stress Testing with wrk

## Configuration
- Tool: wrk | Threads: 8 | Connections: 2000 | Duration: 30s | Timeout: 10s

## Results
| Metric | Value |
|--------|-------|
| Requests/sec | 37.84 |
| Total Requests | 1139 |
| Avg Latency | 5.77s |
| 50th percentile | 5.94s |
| 75th percentile | 7.30s |
| 90th percentile | 8.25s |
| 99th percentile | 9.61s |
| Timeouts | 394 |
| Read errors | 369 |

## Analysis
- At 2000 concurrent connections, throughput is 37.84 req/s — API is under heavy stress
- High average latency (5.77s) indicates the 2-node GKE cluster (1 pod) is CPU-bound
- 394 timeouts (~35%) show the system cannot handle >2000 connections without scaling
- HPA will auto-scale up to 3 pods under sustained load, improving throughput
