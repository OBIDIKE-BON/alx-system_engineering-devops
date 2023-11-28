# File: ssh_config.pp

file { '-/.ssh/config':
  ensure  => present,
  mode    => '0600',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => "# Puppet-managed SSH client configuration\n\nHost 54.208.171.118
  IdentityFile ~/.ssh/school
  PasswordAuthentication no",
}
