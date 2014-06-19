#----------------------------------------------------------------------)
# $Id: mailman.pm,v 1.1 2005/02/16 02:34:26 msoulier Exp $
#----------------------------------------------------------------------
# copyright (C) 2002 Mitel Networks Corporation
#----------------------------------------------------------------------

package esmith::FormMagick::Panel::mailman;

use strict;
use esmith::ConfigDB;
use esmith::FormMagick;

use constant SIGEVENT => '/sbin/e-smith/signal-event';

our @ISA = qw(esmith::FormMagick);
our $VERSION = sprintf '%d.%03d', q$Revision: 1.1 $ =~ /: (\d+).(\d+)/;

=head1 NAME

esmith::FormMagick::Panel::mailman - panel backend

=head1 SYNOPSIS

use esmith::FormMagick::Panel::mailman;

my $panel = esmith::FormMagick::Panel::mailman->new();
$panel->display();

=head1 DESCRIPTION

This class is the esmith::FormMagick subclass for the Mailman panel in the
server manager. It is the backend responsible for handling form submissions,
and helping to output the form itself.

=head2 new

Class constructor.

=cut

sub new
{
    my $class = ref($_[0]) || $_[0];
    my $self = $class->SUPER::new();
    $self->{calling_package} = __PACKAGE__;

    my $db = esmith::ConfigDB->open
        or die "Could not open configuration database";

    $self->{db} = $db;
    $self->debug(0);
    return $self;
}

=head2 get_status

This method returns the current mailman status.

=cut

sub get_status
{
    my $self = shift;
    my $status = $self->{db}->get_prop('mailman', 'status') || 'disabled';
    return $status;
}

=head2 change_settings

This method handles the form submission for the first page.

=cut

sub change_settings
{
    my $self = shift;
    my $q = $self->{cgi};

    my $status = $q->param('status');
    $self->{db}->set_prop('mailman', 'status', $status, type => 'service');

    system(SIGEVENT, 'mailman-update') == 0
        or return $self->error('ERR_UPDATE');

    return $self->success('SUCCESS');
}

1;
