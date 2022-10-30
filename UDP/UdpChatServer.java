import java.io.*;
import java.net.*;
public class UdpChatServer
{
public static DatagramSocket ds;
public static int clientport=789,serverport=790;
public static void main(String args[]) throws Exception
{
byte buffer[] = new byte[10000];
byte bufferS[] = new byte[10000];
int ret=0;
String temp="";
ds=new DatagramSocket(serverport);
BufferedReader dis = new BufferedReader(new InputStreamReader(System.in));
InetAddress ia = InetAddress.getByName("localhost");
while(true)
{
DatagramPacket p =new DatagramPacket(buffer,buffer.length);
ds.receive(p);
String psx = new String(p.getData(),0,p.getLength());
if (psx.equalsIgnoreCase("END"))
{
buffer ="BYE".getBytes();
int len="BYE".length();
ds.send(new DatagramPacket(buffer,len,ia,clientport));
break;
}
System. out.print("Client : "+psx+"\n");
System.out.print("Server : ");
String s=dis.readLine();
bufferS =s.getBytes();
ds.send(new DatagramPacket(bufferS,s.length(),ia,clientport));
}}}
