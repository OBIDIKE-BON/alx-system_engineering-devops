# .pp script to install flask

package { 'installing flask v2.1.0':
  ensure  => installed,
  name    => 'flask',
  command => 'pip3 install flask==2.1.0'
}
