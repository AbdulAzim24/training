int a=0;
TimeSpan time = DateTime.Now.TimeOfDay;            
TimeSpan timer = dateTimePicker2.Value - dateTimePicker1.Value;
MessageBox.Show("Timer set. Device will shutdown in " + timer);
timer = timer + time;            
while (time!=timer)
{
    time = DateTime.Now.TimeOfDay; ;
    if(a==0)
    {
        MessageBox.Show("B");
        a = 1;
    };               
};
if (a == 1)
{
    MessageBox.Show("A");
    a = 0;
}