{ pkgs ? import <nixpkgs> {}}:
let
  inherit (pkgs) mkShell stdenv;
in mkShell {
  # all the command-line tools a developer might need to work in the codebase
  buildInputs = with pkgs; [
    scala-cli
    deno
    jq
    yq
    calc
    metals
    python3
    uv
  ];

  shellHook = ''
    LD_LIBRARY_PATH=${stdenv.cc.cc.lib}/lib/:/run/opengl-driver/lib/
  '';
}
