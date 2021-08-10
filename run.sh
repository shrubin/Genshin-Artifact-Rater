docker stop genshin-artifact-rater-dev
docker rm genshin-artifact-rater-dev

docker run -d \
  --restart unless-stopped \
  --name genshin-artifact-rater-dev \
  -v /opt/genshin-artifact-rater/dev/:/data/ \
  genshin-artifact-rater-dev
