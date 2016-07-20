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

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define "Docker-Flask_Kafka"
  config.vm.box = "adrianovieira/centos7-docker1.12rc4"
  config.vm.box_check_update = false

  # Defining Forwarded Ports
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  # standard sync folder between host and VM (not host shared)
  config.vm.synced_folder ".", "/home/vagrant/sync", type: "rsync"

  # shared folder between host and VM (may be for development porposes)
  config.vm.synced_folder ".", "/home/vagrant/shared"

end # end-of-file
