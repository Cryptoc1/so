# coding: utf-8
require File.expand_path('../lib/mp/version', __FILE__)
require_relative 'lib/mp/version'

Gem::Specification.new do |spec|
  spec.name          = "mp"
  spec.version       = Mp::VERSION
  spec.authors       = ["Josh Trommel"]
  spec.email         = ["joshtrommel@gmail.com"]

  spec.summary       = "CLI for IMDB, basically."
  spec.description   = "Get info on any movie or TV show or whatever, but from your Terminal."
  spec.homepage      = "https://github.com/probablyjosh/mp"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").reject { |f| f.match(%r{^(test|spec|features)/}) }
  spec.bindir        = "exe"
  spec.name	     = "mp"
  spec.executables   = ["mp"]
  spec.require_paths = ["lib"]

  spec.add_development_dependency "bundler", "~> 1.9"
  spec.add_development_dependency "rake", "~> 10.0"

  spec.add_dependency "commander", "~> 4.3.3"
end
