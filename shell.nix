with import <nixpkgs> { };
let
  my-python-packages = python-packages: [
    python-packages.pyyaml
    python-packages.libtorrent-rasterbar
  ];
  my-python = python37.withPackages my-python-packages;
in mkShell { buildInputs = [ bashInteractive my-python libressl ]; }
