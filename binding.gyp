{
  'targets': [
    {
      'target_name': 'gzbz',
      'include_dirs': ['/usr/include', '/usr/local/include'],
      'sources': [ 'compress.cc' ],
      'link_settings': {
          'libraries': [
              '-lbz2'
          ]
      },
      'cflags': [
        '-D_FILE_OFFSET_BITS=64',
        '-D_LARGEFILE_SOURCE',
        '-Wall'
      ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'conditions': [
        ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
          }
        }]
      ],
    }
  ]
}
