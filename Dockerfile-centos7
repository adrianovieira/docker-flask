FROM centos:7

MAINTAINER Adriano Vieira <adriano.svieira at gmail.com>

# install base packs
# apache.wsgi python pip
RUN yum -y install epel-release; \
    yum -y install python-pip httpd mod_wsgi; yum clean all;

# Simple startup script to avoid some issues observed with container restart (CentOS tip)
ADD setup/run-apache-httpd.sh /run-apache-httpd.sh
RUN chmod -v +x /run-apache-httpd.sh

# setup apache default wsgi vhost
COPY setup/httpd-vhost-wsgi.conf /etc/httpd/conf.d/welcome.conf

# expose apache port
EXPOSE 80

# pip install app requirements
COPY code/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# upload app to image
ADD code /var/www/html
WORKDIR /var/www/html

# run flask app on apache
CMD ["/run-apache-httpd.sh"]
