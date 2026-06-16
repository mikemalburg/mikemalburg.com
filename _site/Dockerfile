# Build: docker build -t mikemalburg .
# Run: docker run -p 4000:4000 mikemalburg
# Deploy to S3:
#   1. docker run --rm -v $(pwd):/site mikemalburg tar czf /tmp/site.tar.gz _site
#   2. Upload site.tar.gz to S3 and extract

FROM jekyll/jekyll:latest AS build
WORKDIR /site
COPY . .
RUN bundle config set path 'vendor/bundle' && bundle install && jekyll build

FROM nginx:alpine
COPY --from=build /site/_site /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
