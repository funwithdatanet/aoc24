{
  description = "Flake for funwithdata.net";

  nixConfig.bash-prompt = "\[funwithdata.net\]> ";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/release-24.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages."${system}";
        inherit (pkgs) mkShell;
      in
      {
        overlay = final: prev: {
        };

        devShell = import ./shell.nix { inherit pkgs; };
      }
    );

}
