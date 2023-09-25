#!/usr/bin/pup
# Using Puppet, install flask from pip3

package { 'python3-pip':
  ensure => 'installed',
}

exec { 'install_flask':
  command => 'pip3 install Flask==2.1.0',
  path    => ['/usr/bin', '/usr/local/bin'],
  require => Package['python3-pip'],
}

