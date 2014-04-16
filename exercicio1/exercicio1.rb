#!/usr/bin/ruby


file_keys = File.open("keys")
file_keys.each do |key|
    system("gpg --recv-key #{key}")
    system("gpg --sign-key #{key}")
end
