# File: ssh_config.pp
include stdlib

file{'ssh_config':
   path => '/home/ubuntu/.ssh/ssh_config',
   ensure => present
}

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/home/ubuntu/.ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'Delare identity file':
  ensure => present,
  path   => '/home/ubuntu/.ssh/ssh_config',
  line   => '     IdentityFile ~/.ssh/school',
  replace => true,
}
