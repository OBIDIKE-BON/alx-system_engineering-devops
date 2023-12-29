# pp script to install flask
package {'python3':
  ensure   => present,
}

package {'pip3':
  ensure   => present,
}

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
