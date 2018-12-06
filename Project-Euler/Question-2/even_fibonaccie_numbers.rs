fn main()
{
    let million = 4000000;
    let mut total = 0 ;
    let mut a = 1;
    let mut b = 1;


    while a+b <= million
    {
        let  c = a + b;
        if c % 2 == 0
        {
            total = total + c 
        }
        // b,a = c,b;
        a = b; 
        b = c;
    }
    println!("{}", total)
}