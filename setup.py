#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
	name = 'portablelinux',
	version = '0.9.2',
	description = 'A bootable USB Live Linux creator',
	long_description = """Portable Linux is a tool that lets you create bootable USB and removable drives using popular Live CDs based on Casper.""",
	author = 'Manuel Amador (Rudd-O)',
	author_email = 'rudd-o@rudd-o.com',
	license = "GPL",
	url = 'http://rudd-o.com/new-projects/portablelinux',
	data_files = [
		('share/portablelinux', [
			'portablelinux.glade',
			'portablelinux.png'
			]),
		('share/pixmaps', ['portablelinux.png']),
		('share/applications', ['portablelinux.desktop']),
	],
	scripts = ["portablelinux"],
	keywords = "usb removable linux live cd installer",
)
