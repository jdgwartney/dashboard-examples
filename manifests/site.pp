# Explictly set to avoid warning message
Package {
  allow_virtual => false,
}

file { 'bash_profile':
  path    => '/home/vagrant/.bash_profile',
  ensure  => file,
  source  => '/vagrant/manifests/bash_profile',
  require => Exec['update-packages'],
}

class { 'boundary':
  token => $api_token,
  require => Exec['update-packages'],
}

file { "/var/www/html/dashboards":
  source  => "/vagrant/dashboards",
  recurse => true,
}

exec { 'update-packages':
  command => '/usr/bin/apt-get update -y',
}

package { 'apache2':
  require => Exec['update-packages'],
}

service { 'apache2':
  ensure => 'running',
  require => Package['apache2'],
}

