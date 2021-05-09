FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
RUN mkdir /etc/nginx/ssl
COPY ssl_key.key /etc/nginx/ssl
COPY ssl_crt.crt /etc/nginx/ssl