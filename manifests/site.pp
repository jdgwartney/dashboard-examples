# Explictly set to avoid warning message
Package {
  allow_virtual => false,
}

file { 'bash_profile':
  path    => '/home/vagrant/.bash_profile',
  ensure  => file,
  source  => '/vagrant/manifests/bash_profile',
}

class { 'boundary':
  token => $api_token,
}

# TODO: Update meter.conf and restart service
#file { 'update-meter-conf':
#  notify  => Service['boundary-meter'],
#  path    => '/etc/boundary/meter.conf',
#  mode    => '0644',
#  owner   => 'root',
#  group   => 'root',
#  ensure  => file,
#  source  => '/vagrant/manifests/meter.conf',
#}

file { "/var/www/html/dashboards":
  source  => "/vagrant/dashboards",
  recurse => true,
  require => Package['apache2'],
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

