set ns [new Simulator]
set nf [open out.nam w]
$ns namtrace-all $nf
set tr [open out.tr w]
$ns trace-all $tr
proc finish {} {
global nf ns tr
$ns flush-trace
close $tr
exec nam out.nam &
exit 0
}
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
$ns duplex-link $n0 $n1 10Mb 10ms DropTail
$ns duplex-link $n0 $n2 10Mb 10ms DropTail
$ns duplex-link $n1 $n2 10Mb 15ms DropTail
$ns duplex-link $n1 $n3 10Mb 10ms DropTail
$ns duplex-link $n2 $n3 10Mb 15ms DropTail
$ns duplex-link $n2 $n4 10Mb 30ms DropTail
$ns duplex-link $n3 $n5 10Mb 10ms DropTail 
$ns duplex-link $n3 $n4 10Mb 10ms DropTail
$ns duplex-link $n4 $n5 10Mb 10ms DropTail
$ns duplex-link-op $n0 $n1 orient right-up
$ns duplex-link-op $n0 $n2 orient right-down
$ns duplex-link-op $n1 $n2 orient down
$ns duplex-link-op $n1 $n3 orient right
$ns duplex-link-op $n2 $n3 orient right-up
$ns duplex-link-op $n2 $n4 orient right
$ns duplex-link-op $n3 $n4 orient down
$ns duplex-link-op $n3 $n5 orient right-down
$ns duplex-link-op $n4 $n5 orient right-up
set tcp [new Agent/TCP]
$tcp set class_ 2
$ns attach-agent $n0 $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n5 $sink
$ns connect $tcp $sink
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP
$ftp set packet_size_ 1000
$ftp set rate_ 1mb
$ns rtproto DV
$ns at 0.5 "$ftp start"
$ns rtmodel-at 1.0 down $n1 $n3
$ns rtmodel-at 2.0 down $n0 $n2
$ns rtmodel-at 3.0 up $n1 $n3
$ns rtmodel-at 3.0 up $n0 $n2
$ns at 4.5 "$ftp stop"
$ns at 5.0 "finish"
$ns run