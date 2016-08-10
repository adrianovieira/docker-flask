'''
/**
 * Tasting docker in swarm mode (1.12+)
 *
 * Vagrantfile for Linux Containers Docker-Swarm (Operating System Level Virtualization)
 * and also for tasting python Flask application (over apache/httpd) on docker images
 * @author Adriano Vieira <adriano.svieira at gmail.com>
 * @license @see LICENCE
 */
 '''

VAGRANTFILE_API_VERSION = "2"
Vagrant.require_version ">= 1.7.2"

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version. Please don't change it unless you know what
# you're doing.
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define "Docker-Flask"
  config.vm.box = "adrianovieira/centos7-docker1.12-GA"
  config.vm.box_check_update = false

  # shared folder between host and VM (may be for development porposes)
  config.vm.synced_folder ".", "/home/vagrant/shared"

  # Defining Forwarded Ports
  config.vm.network "forwarded_port", guest: 80, host: 8080 #, auto_correct: true
  config.vm.network "forwarded_port", guest: 5000, host: 5000 #, auto_correct: true

  config.vm.provider "virtualbox" do |vb|
     #vb.gui = true
     #vb.memory = "4096"
     #vb.cpus = 2
     vb.name = "Docker-Flask"
  end

  # Setting Systemd docker proxy
  #  (also check my vagrant setup on https://gitlab.com/snippets/22859
  #   or https://gist.github.com/adrianovieira/32ebf370df2df78fcaa930db30e521d1)
  config.vm.provision "docker-setup-proxy", type: "shell",
          path: "docker-setup-proxy.sh"
end # end-of-file
