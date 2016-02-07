# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "puppetlabs/ubuntu-14.04-64-puppet"
  config.vm.box_version = "1.0.1"

  config.vm.network "forwarded_port", guest: 80, host: 8100

  config.vm.provision :shell do |shell|
     shell.inline = "puppet module install puppetlabs-stdlib;
                     puppet module install puppetlabs-apt;
                     puppet module install boundary-boundary;
                     exit 0"
  end

  config.vm.provision "puppet" do |puppet|
      puppet.manifests_path = "manifests"
      puppet.manifest_file  = "site.pp"
      puppet.facter = {
         "api_token" => ENV["API_TOKEN"]
      }
  end
end
