# kill a process
exec { 'pkill killmenow':
  command  => 'pkill killmenow',
  provider => shell
}
