# .pp script to install flask

  exec { 'install_flask':
    command => 'pip3 install flask==2.1.0',
    # Only run if the package python3-pip is installed successfully
    require => Package['python3-pip'],
    # Don't run if Flask is already installed and at the correct version
    unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  }
