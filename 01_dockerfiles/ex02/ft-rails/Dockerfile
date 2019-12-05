FROM ruby:2.5.1

RUN apt-get update && apt-get install -y nodejs
RUN gem install rails --version 5.2.0

ENV RAILS_ENV development

# Copy applicaiton code
RUN mkdir -p /opt/app
COPY ./app /opt/app

# Change to the application's current directory
ONBUILD WORKDIR /opt/app
ONBUILD RUN bundle install
ONBUILD RUN rake db:create db:migrate db:seed

# docker buid . -t ft-rails:on-build
# docker run -it --rm ft-rails:on-build
