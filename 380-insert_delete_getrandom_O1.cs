public class RandomizedSet {
    private Dictionary<int, int> d;
    private List<int> l;
    private Random rnd;

    public RandomizedSet()
    {
        this.d = new();
        this.l = new();
        this.rnd = new();
    }
    
    public bool Insert(int val)
    {
        if (!this.d.ContainsKey(val))
        {
            this.d[val] = this.l.Count();
            this.l.Add(val);
            return true;
        }

        return false;
    }
    
    public bool Remove(int val)
    {
        if (this.d.ContainsKey(val))
        {
            int posInL = this.d[val];
            int last = this.l[this.l.Count() - 1];

            (this.d[last], this.l[posInL]) = (posInL, last);

            this.d.Remove(val);
            this.l.RemoveAt(this.l.Count() - 1);
            
            return true;
        }
        return false;
    }
    
    public int GetRandom()
    {
        return this.l[rnd.Next(0, this.l.Count())];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.Insert(val);
 * bool param_2 = obj.Remove(val);
 * int param_3 = obj.GetRandom();
 */
