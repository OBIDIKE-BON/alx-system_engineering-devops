# .pp script to install flask

package {'flask':
  ensure => 'present',
}

exec { 'install_flask':
  command  => 'sudo pip3 install flask==2.1.0',
  provider => shell,
}
