FROM ruby:2.5.1

RUN apt-get update && apt-get install -y mysql-client sqlite3 --no-install-recommends
RUN gem install rails --version 5.2.0

ENV RAILS_ENV development
# Copy applicaiton code
COPY ./app /opt/app

# Change to the application's current directory
WORKDIR /opt/app

RUN bundle install
RUN rake db:migrate && rake db:seed
