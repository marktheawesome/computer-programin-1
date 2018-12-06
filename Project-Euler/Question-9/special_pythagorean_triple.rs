fn pythagorean_triple(a:i32,b:i32,c:i32) ->bool
{
    let c = c*c;
    if c == ((a*a)+ (b*b))
    {
        return true;
    }
    else
    {
        return false;
    } 
}

fn main()
{
    let i = 1000;
    let mut a = 1;
    let mut b = 1;
    let mut c = 1;
    while a  < i/3
    {
        b = 1;
        while b< i/2
        {
            c = i-(a+b);
            if a+b+c == i && pythagorean_triple(a,b,c)
            {
                break;
            }
            b = b+1;
        }
        if a+b+c == i && pythagorean_triple(a,b,c)
        {
            break;
        }
        a = a + 1;
    }
    let d = a*b*c;
    println!("{}",a);
    // println!("\n");
    println!("{}",b);
    // println!("\n");
    println!("{}",c);
    // println!("\n");
    println!("{}",d);
    // println!("\n");

}