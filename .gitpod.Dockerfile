FROM gitpod/workspace-full:latest

RUN curl https://cli-assets.heroku.com/install.sh | sh
RUN wget https://cli-assets.heroku.com/install.sh -O install-heroku.sh && \
    sh install-heroku.sh