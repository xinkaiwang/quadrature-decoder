{
  "targets": [
    {
      "target_name": "hello",
      "sources": [ "hello.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ]
    },
    {
      "target_name": "isr",
      "sources": [ "isr.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        'wiringpi/wiringPi',
        'wiringpi/devLib'
      ],
      'libraries': [
        '<!(pwd)/../wiringPi/wiringPi/libwiringPi.a',
        '<!(pwd)/../wiringPi/devLib/libwiringPiDev.a'
      ]
    }

  ]
}