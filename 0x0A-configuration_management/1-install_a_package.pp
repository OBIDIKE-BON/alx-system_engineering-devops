# .pp script to install flask

package {'flask':
  ensure   => installed,
  provider => pip3
}
