# .pp script to install flask

package {'flask':
  ensure   => '2.1.0',
  command  => '/usr/bin/pip3',
  provider => pip3,
}
