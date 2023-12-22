# .pp script to install flask

  package { 'flask':
    ensur   => '2.1.0',
    provider => 'pip3',
    require  => Package['python3-pip'],
  }
