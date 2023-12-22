# .pp script to install flask

  package { 'flask':
    ensure   => installed,
    command  => 'pip3 install flask==2.1.0',
    provider => 'pip3',
  }
