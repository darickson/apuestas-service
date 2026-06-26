# apuestas-service

Microservicio de apuestas deportivas del casino (FastAPI). Comparte la base de
datos PostgreSQL y el JWT_SECRET con casino-backend. Lista eventos con cuotas
1X2, registra apuestas, simula el partido (modelo Poisson) y liquida las
apuestas.

- Prefijo de rutas: /api/apuestas - Docs: /docs

## Endpoints
- GET /api/apuestas/eventos
- POST /api/apuestas
- GET /api/apuestas/mis-apuestas
- POST /api/apuestas/eventos/{id}/simular
- POST /api/apuestas/reiniciar

## Entregables implementados
1. Rutas de salud /livez y /readyz para Kubernetes.
2. Dockerfile multi-stage con usuario no root.
3. Workflow de CI/CD (GitHub Actions): build, push a ECR, deploy en EKS.
4. Manifiestos de Kubernetes (Deployment + Service) con probes.
5. Pruebas de carga con k6.
