# Ansible-DigitalOcean Playbooks

  This is an Ansible playbook used for managing my website www.antonioalaniz.com. This was tested against Ubuntu 16.04 (Xenial) using Vagrant and pushed live to DigitalOcean.

## Playbooks

* `provision.yml`: Updates the `apt` repo and installs Python2
* `setup-vagrant.yml`: Creates a non-root user and group, elevates sudo permissions, allows passwordless sudo. These tasks are also available in the `common-vagrant` role listed below
* `dev-deploy.yml` and `live-deploy.yml`: installs pelican, nginx, sets up firewall rules for live and development machines
* `dev-update-blog.yml` and `live-update-blog.yml`: deletes and re-installs the blogs to update new entries. This playbook does not perform the the `common-vagrant`, `pelican-nginx`, `ansible-nginx` and `wtanaka.certbot` roles.

## Roles

  These playbooks utilize the following roles:

  * [`ansible-ufw`](https://github.com/talaniz/ansible-ufw): closes the firewall and allows only the `access_ports` listed in the variables below
  * [`common-vagrant`](https://github.com/talaniz/common-vagrant): a series of common tasks to set up the Vagrant environment for testing
  * [`pelican-nginx`](https://github.com/talaniz/pelican-nginx): a role for setting up Pelican to work with nginx
  * [`pelican-vagrant`](https://github.com/talaniz/pelican-vagrant): adds Pelican to a Vagrant or live Digitalocean droplet
  * [`wtanaka.certbot`](https://github.com/wtanaka/ansible-role-certbot): a role by Wesley Tanaka that automates letsencrypt certificate generation


## Variables

* `home_dir`: home directory for the non-root user
* `pelican_env`: directory where virtualenv is installed
* `pelican_themes`: location of pelican themes to be installed
* `web_root`: /var/www/antonioalaniz.com
* `blog_repo`: https://github.com/talaniz/antonioalaniz.com.git
* `nginx`: location of nginx
* `blog_template_dir`: location of the blog template in `{{pelican_themes}}``
* `files_dir`: directory containing all files to be copied to the remote machine
* `templates_dir`: directory containing all templates to be copied
* `domain`: website domain (ex. antonioalaniz.com)
* `www_domain`: domain with www added (ex. www.antonioalaniz.com)
* `access_ports`: ports to be opened on the firewall
* `ssh_port`: port to connect to the remote machine via ssh
* `email`: an email address to be used to generate certifications (dev only)
* `ssl_cert`: location letsencrypt generates the ssl certificate--/etc/letsencrypt/live/{{www_domain}}/fullchain.pem
* `ssl_cert_key`: location letsencrypt generates the ssl certificate /etc/letsencrypt/live/{{domain}}/privkey.pem
* `letsencrypt_email`: an email address to be used to generate certifications (live only)
* `letsencrypt_webroot`: location of web root for letsencrypt to generate cert
* `letsencrypt_fake_key`: If set to true (dev only), the letsencrypt role will copy fake pem files instead of generating a certificate
* `letsencrypt_renew_by_default`: option to renew letsencrypt certificates
* `letsencrypt_domains`: domains letsencrypt will use to generate certificates
* `google_analytics`: Google Analytics ID to use for tracking

## Installation

1. Clone the repository: git clone https://github.com/talaniz/ansible-pelican.git
2. Install requirements: pip install -r requirements.txt
3. Create a variables file and populate the variables above
4. Install roles: mkdir roles && cd roles, then clone/install roles--
    * git clone https://github.com/talaniz/common-vagrant.git
    * git clone https://github.com/talaniz/ansible-ufw.git
    * git clone https://github.com/talaniz/pelican-nginx.git
    * ansible-galaxy install wtanaka.certbot
5. Use the `Vagrantfile` to create the virtual environment: vagrant up
6. Run the `dev-deploy.yml` file: ansible-playbook playbooks/dev-deploy.yml

## To Do:

* Clean up `files` and `templates` to only include used files (some included for development)
