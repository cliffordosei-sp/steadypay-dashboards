#!/bin/bash
# Deploy Steadypay Hub to Cloud Run
# Usage: ./deploy.sh

set -e

PROJECT_ID="steadypay-189320"
REGION="europe-west2"
SERVICE_NAME="steadypay-hub"
REPO="europe-west2-docker.pkg.dev/${PROJECT_ID}/steadypay"
TAG=$(date +%Y%m%d%H%M%S)
IMAGE="${REPO}/${SERVICE_NAME}:${TAG}"

echo "🔨 Building image: ${IMAGE}"
docker build --platform linux/amd64 -t "${IMAGE}" .

echo "📤 Pushing image..."
docker push "${IMAGE}"

echo "🚀 Deploying to Cloud Run..."
gcloud run deploy "${SERVICE_NAME}" \
  --image "${IMAGE}" \
  --platform managed \
  --region "${REGION}" \
  --project "${PROJECT_ID}" \
  --port 8080 \
  --memory 512Mi \
  --cpu 1 \
  --min-instances 0 \
  --max-instances 2 \
  --no-allow-unauthenticated

echo "✅ Done. To access the hub:"
echo "   gcloud run services proxy ${SERVICE_NAME} --project ${PROJECT_ID} --region ${REGION}"
