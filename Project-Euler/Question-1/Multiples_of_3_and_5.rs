fn main()
{
    let mut current_number = 1;
    let mut total = 0;
    let upper_number = 1000;
    
    while current_number < upper_number
    {
        if current_number %3 == 0 || current_number % 5 == 0
        {
            total = total + current_number;
        } 
        
        current_number = current_number + 1
    }
    
    println!("{}",total);
}
